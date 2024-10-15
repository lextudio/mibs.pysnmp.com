# SNMP MIB module (LANNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:11 2024
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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

_Lannet_ObjectIdentity = ObjectIdentity
lannet = _Lannet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 7)
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
          ("unknown", 255))
    )


_ChHWType_Type.__name__ = "Integer32"
_ChHWType_Object = MibScalar
chHWType = _ChHWType_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 7),
    _ChReset_Type()
)
chReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chReset.setStatus("mandatory")
_ChFullConfig_Type = OctetString
_ChFullConfig_Object = MibScalar
chFullConfig = _ChFullConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 8),
    _ChFullConfig_Type()
)
chFullConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFullConfig.setStatus("mandatory")
_ChAg_ObjectIdentity = ObjectIdentity
chAg = _ChAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 7, 9)
)
_ChGenAgTable_Object = MibTable
chGenAgTable = _ChGenAgTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1)
)
if mibBuilder.loadTexts:
    chGenAgTable.setStatus("mandatory")
_ChGenAgEntry_Object = MibTableRow
chGenAgEntry = _ChGenAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1)
)
chGenAgEntry.setIndexNames(
    (0, "LANNET-MIB", "chGenAgId"),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1, 1),
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("ielb", 7),
          ("itlb", 8),
          ("lts16", 9),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1, 4),
    _ChGenAgAddr_Type()
)
chGenAgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgAddr.setStatus("mandatory")
_ChGenAgSpecificOID_Type = ObjectIdentifier
_ChGenAgSpecificOID_Object = MibTableColumn
chGenAgSpecificOID = _ChGenAgSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 1, 1, 5),
    _ChGenAgSpecificOID_Type()
)
chGenAgSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgSpecificOID.setStatus("mandatory")
_ChLntAgTable_Object = MibTable
chLntAgTable = _ChLntAgTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2)
)
if mibBuilder.loadTexts:
    chLntAgTable.setStatus("mandatory")
_ChLntAgEntry_Object = MibTableRow
chLntAgEntry = _ChLntAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1)
)
chLntAgEntry.setIndexNames(
    (0, "LANNET-MIB", "chLntAgId"),
)
if mibBuilder.loadTexts:
    chLntAgEntry.setStatus("mandatory")


class _ChLntAgId_Type(Integer32):
    """Custom type chLntAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChLntAgId_Type.__name__ = "Integer32"
_ChLntAgId_Object = MibTableColumn
chLntAgId = _ChLntAgId_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 1),
    _ChLntAgId_Type()
)
chLntAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgId.setStatus("mandatory")
_ChLntAgSLIPAddress_Type = IpAddress
_ChLntAgSLIPAddress_Object = MibTableColumn
chLntAgSLIPAddress = _ChLntAgSLIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 2),
    _ChLntAgSLIPAddress_Type()
)
chLntAgSLIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgSLIPAddress.setStatus("mandatory")
_ChLntAgSWVersion_Type = OctetString
_ChLntAgSWVersion_Object = MibTableColumn
chLntAgSWVersion = _ChLntAgSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 3),
    _ChLntAgSWVersion_Type()
)
chLntAgSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgSWVersion.setStatus("mandatory")
_ChLntAgKernelVersion_Type = OctetString
_ChLntAgKernelVersion_Object = MibTableColumn
chLntAgKernelVersion = _ChLntAgKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 4),
    _ChLntAgKernelVersion_Type()
)
chLntAgKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgKernelVersion.setStatus("mandatory")
_ChLntAgCoprocSWVersion_Type = OctetString
_ChLntAgCoprocSWVersion_Object = MibTableColumn
chLntAgCoprocSWVersion = _ChLntAgCoprocSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 5),
    _ChLntAgCoprocSWVersion_Type()
)
chLntAgCoprocSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgCoprocSWVersion.setStatus("mandatory")
_ChLntAgSWFault_Type = OctetString
_ChLntAgSWFault_Object = MibTableColumn
chLntAgSWFault = _ChLntAgSWFault_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 6),
    _ChLntAgSWFault_Type()
)
chLntAgSWFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgSWFault.setStatus("mandatory")
_ChLntAgMgmtBusSelection_Type = Integer32
_ChLntAgMgmtBusSelection_Object = MibTableColumn
chLntAgMgmtBusSelection = _ChLntAgMgmtBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 7),
    _ChLntAgMgmtBusSelection_Type()
)
chLntAgMgmtBusSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgMgmtBusSelection.setStatus("mandatory")


class _ChLntAgCoprocCommStatus_Type(Integer32):
    """Custom type chLntAgCoprocCommStatus based on Integer32"""
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


_ChLntAgCoprocCommStatus_Type.__name__ = "Integer32"
_ChLntAgCoprocCommStatus_Object = MibTableColumn
chLntAgCoprocCommStatus = _ChLntAgCoprocCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 8),
    _ChLntAgCoprocCommStatus_Type()
)
chLntAgCoprocCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgCoprocCommStatus.setStatus("mandatory")


class _ChLntAgCommDebugMode_Type(Integer32):
    """Custom type chLntAgCommDebugMode based on Integer32"""
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


_ChLntAgCommDebugMode_Type.__name__ = "Integer32"
_ChLntAgCommDebugMode_Object = MibTableColumn
chLntAgCommDebugMode = _ChLntAgCommDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 9),
    _ChLntAgCommDebugMode_Type()
)
chLntAgCommDebugMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgCommDebugMode.setStatus("mandatory")


class _ChLntAgConfigChangeTraps_Type(Integer32):
    """Custom type chLntAgConfigChangeTraps based on Integer32"""
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


_ChLntAgConfigChangeTraps_Type.__name__ = "Integer32"
_ChLntAgConfigChangeTraps_Object = MibTableColumn
chLntAgConfigChangeTraps = _ChLntAgConfigChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 10),
    _ChLntAgConfigChangeTraps_Type()
)
chLntAgConfigChangeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgConfigChangeTraps.setStatus("mandatory")


class _ChLntAgFaultTraps_Type(Integer32):
    """Custom type chLntAgFaultTraps based on Integer32"""
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


_ChLntAgFaultTraps_Type.__name__ = "Integer32"
_ChLntAgFaultTraps_Object = MibTableColumn
chLntAgFaultTraps = _ChLntAgFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 11),
    _ChLntAgFaultTraps_Type()
)
chLntAgFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgFaultTraps.setStatus("mandatory")


class _ChLntAgTrafficThreshTraps_Type(Integer32):
    """Custom type chLntAgTrafficThreshTraps based on Integer32"""
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


_ChLntAgTrafficThreshTraps_Type.__name__ = "Integer32"
_ChLntAgTrafficThreshTraps_Object = MibTableColumn
chLntAgTrafficThreshTraps = _ChLntAgTrafficThreshTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 12),
    _ChLntAgTrafficThreshTraps_Type()
)
chLntAgTrafficThreshTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgTrafficThreshTraps.setStatus("mandatory")


class _ChLntAgGroupEnrollDeenrollTraps_Type(Integer32):
    """Custom type chLntAgGroupEnrollDeenrollTraps based on Integer32"""
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


_ChLntAgGroupEnrollDeenrollTraps_Type.__name__ = "Integer32"
_ChLntAgGroupEnrollDeenrollTraps_Object = MibTableColumn
chLntAgGroupEnrollDeenrollTraps = _ChLntAgGroupEnrollDeenrollTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 13),
    _ChLntAgGroupEnrollDeenrollTraps_Type()
)
chLntAgGroupEnrollDeenrollTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgGroupEnrollDeenrollTraps.setStatus("mandatory")


class _ChLntAgSoftFaultTraps_Type(Integer32):
    """Custom type chLntAgSoftFaultTraps based on Integer32"""
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


_ChLntAgSoftFaultTraps_Type.__name__ = "Integer32"
_ChLntAgSoftFaultTraps_Object = MibTableColumn
chLntAgSoftFaultTraps = _ChLntAgSoftFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 14),
    _ChLntAgSoftFaultTraps_Type()
)
chLntAgSoftFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgSoftFaultTraps.setStatus("mandatory")


class _ChLntAgHubEnrollTraps_Type(Integer32):
    """Custom type chLntAgHubEnrollTraps based on Integer32"""
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


_ChLntAgHubEnrollTraps_Type.__name__ = "Integer32"
_ChLntAgHubEnrollTraps_Object = MibTableColumn
chLntAgHubEnrollTraps = _ChLntAgHubEnrollTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 15),
    _ChLntAgHubEnrollTraps_Type()
)
chLntAgHubEnrollTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgHubEnrollTraps.setStatus("mandatory")


class _ChLntAgTempThreshTraps_Type(Integer32):
    """Custom type chLntAgTempThreshTraps based on Integer32"""
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


_ChLntAgTempThreshTraps_Type.__name__ = "Integer32"
_ChLntAgTempThreshTraps_Object = MibTableColumn
chLntAgTempThreshTraps = _ChLntAgTempThreshTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 16),
    _ChLntAgTempThreshTraps_Type()
)
chLntAgTempThreshTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgTempThreshTraps.setStatus("mandatory")
_ChLntAgSpecificOID_Type = ObjectIdentifier
_ChLntAgSpecificOID_Object = MibTableColumn
chLntAgSpecificOID = _ChLntAgSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 17),
    _ChLntAgSpecificOID_Type()
)
chLntAgSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgSpecificOID.setStatus("mandatory")
_ChLntAgLastAddrConfig_Type = OctetString
_ChLntAgLastAddrConfig_Object = MibTableColumn
chLntAgLastAddrConfig = _ChLntAgLastAddrConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 18),
    _ChLntAgLastAddrConfig_Type()
)
chLntAgLastAddrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgLastAddrConfig.setStatus("mandatory")
_ChLntAgSecAddrConfig_Type = OctetString
_ChLntAgSecAddrConfig_Object = MibTableColumn
chLntAgSecAddrConfig = _ChLntAgSecAddrConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 19),
    _ChLntAgSecAddrConfig_Type()
)
chLntAgSecAddrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgSecAddrConfig.setStatus("mandatory")


class _ChLntAgSoftwareStatus_Type(Integer32):
    """Custom type chLntAgSoftwareStatus based on Integer32"""
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


_ChLntAgSoftwareStatus_Type.__name__ = "Integer32"
_ChLntAgSoftwareStatus_Object = MibTableColumn
chLntAgSoftwareStatus = _ChLntAgSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 20),
    _ChLntAgSoftwareStatus_Type()
)
chLntAgSoftwareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgSoftwareStatus.setStatus("mandatory")


class _ChLntAgConfigurationSymbol_Type(OctetString):
    """Custom type chLntAgConfigurationSymbol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ChLntAgConfigurationSymbol_Type.__name__ = "OctetString"
_ChLntAgConfigurationSymbol_Object = MibTableColumn
chLntAgConfigurationSymbol = _ChLntAgConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 21),
    _ChLntAgConfigurationSymbol_Type()
)
chLntAgConfigurationSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chLntAgConfigurationSymbol.setStatus("mandatory")
_ChLntAgIntTemp_Type = Integer32
_ChLntAgIntTemp_Object = MibTableColumn
chLntAgIntTemp = _ChLntAgIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 22),
    _ChLntAgIntTemp_Type()
)
chLntAgIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgIntTemp.setStatus("mandatory")
_ChLntAgBootVersion_Type = OctetString
_ChLntAgBootVersion_Object = MibTableColumn
chLntAgBootVersion = _ChLntAgBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 9, 2, 1, 23),
    _ChLntAgBootVersion_Type()
)
chLntAgBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLntAgBootVersion.setStatus("mandatory")
_ChMgr_ObjectIdentity = ObjectIdentity
chMgr = _ChMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 7, 10)
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
    (1, 3, 6, 1, 4, 1, 81, 7, 10, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 10, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 10, 3),
    _ChMgrMngmtState_Type()
)
chMgrMngmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chMgrMngmtState.setStatus("mandatory")
_ChHW_ObjectIdentity = ObjectIdentity
chHW = _ChHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 7, 11)
)
_ChHWPSUTable_Object = MibTable
chHWPSUTable = _ChHWPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1)
)
if mibBuilder.loadTexts:
    chHWPSUTable.setStatus("mandatory")
_ChHWPSUEntry_Object = MibTableRow
chHWPSUEntry = _ChHWPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1, 1)
)
chHWPSUEntry.setIndexNames(
    (0, "LANNET-MIB", "chHWPSUId"),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1, 1, 3),
    _ChHWPSULocation_Type()
)
chHWPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPSULocation.setStatus("mandatory")
_ChHWPSUVoltage_Type = Integer32
_ChHWPSUVoltage_Object = MibTableColumn
chHWPSUVoltage = _ChHWPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 2),
    _ChHWIntTempWarning_Type()
)
chHWIntTempWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWIntTempWarning.setStatus("mandatory")
_ChHWIntTempThresh_Type = Integer32
_ChHWIntTempThresh_Object = MibScalar
chHWIntTempThresh = _ChHWIntTempThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 3),
    _ChHWIntTempThresh_Type()
)
chHWIntTempThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chHWIntTempThresh.setStatus("mandatory")
_ChHWPeakIntTemp_Type = Integer32
_ChHWPeakIntTemp_Object = MibScalar
chHWPeakIntTemp = _ChHWPeakIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 81, 7, 11, 4),
    _ChHWPeakIntTemp_Type()
)
chHWPeakIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPeakIntTemp.setStatus("mandatory")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 8)
)
_GenGroupTable_Object = MibTable
genGroupTable = _GenGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1)
)
if mibBuilder.loadTexts:
    genGroupTable.setStatus("mandatory")
_GenGroupEntry_Object = MibTableRow
genGroupEntry = _GenGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1)
)
genGroupEntry.setIndexNames(
    (0, "LANNET-MIB", "genGroupId"),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 1),
    _GenGroupId_Type()
)
genGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupId.setStatus("mandatory")
_GenGroupSWVersion_Type = OctetString
_GenGroupSWVersion_Object = MibTableColumn
genGroupSWVersion = _GenGroupSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 2),
    _GenGroupSWVersion_Type()
)
genGroupSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSWVersion.setStatus("mandatory")
_GenGroupKernelVersion_Type = OctetString
_GenGroupKernelVersion_Object = MibTableColumn
genGroupKernelVersion = _GenGroupKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 3),
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("ielb", 29),
          ("itlb", 44),
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
          ("le120r", 46),
          ("le120r-2", 47),
          ("le140xt", 28),
          ("le140xtc", 48),
          ("le140xtf", 45),
          ("le140xtf-fb", 55),
          ("le140xtn", 67),
          ("le140xtq", 52),
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
          ("le80xt", 27),
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
          ("llt8", 36),
          ("ltr104-D25", 40),
          ("ltr104-D9", 39),
          ("ltr104-RJ45", 34),
          ("ltr104f", 43),
          ("ltr104s", 56),
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
          ("unknown", 255))
    )


_GenGroupType_Type.__name__ = "Integer32"
_GenGroupType_Object = MibTableColumn
genGroupType = _GenGroupType_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 4),
    _GenGroupType_Type()
)
genGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupType.setStatus("mandatory")


class _GenGroupDescr_Type(OctetString):
    """Custom type genGroupDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenGroupDescr_Type.__name__ = "OctetString"
_GenGroupDescr_Object = MibTableColumn
genGroupDescr = _GenGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 9),
    _GenGroupAutoMan_Type()
)
genGroupAutoMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupAutoMan.setStatus("mandatory")
_GenGroupFullConfig_Type = OctetString
_GenGroupFullConfig_Object = MibTableColumn
genGroupFullConfig = _GenGroupFullConfig_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 18),
    _GenGroupSupplyVoltageFault_Type()
)
genGroupSupplyVoltageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSupplyVoltageFault.setStatus("mandatory")
_GenGroupIntTemp_Type = Integer32
_GenGroupIntTemp_Object = MibTableColumn
genGroupIntTemp = _GenGroupIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 19),
    _GenGroupIntTemp_Type()
)
genGroupIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupIntTemp.setStatus("mandatory")
_GenGroupSpecificOID_Type = ObjectIdentifier
_GenGroupSpecificOID_Object = MibTableColumn
genGroupSpecificOID = _GenGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 20),
    _GenGroupSpecificOID_Type()
)
genGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSpecificOID.setStatus("mandatory")


class _GenGroupConfigurationSymbol_Type(OctetString):
    """Custom type genGroupConfigurationSymbol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GenGroupConfigurationSymbol_Type.__name__ = "OctetString"
_GenGroupConfigurationSymbol_Object = MibTableColumn
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 81, 8, 1, 1, 21),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("mandatory")
_GenPort_ObjectIdentity = ObjectIdentity
genPort = _GenPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 9)
)
_GenPortTable_Object = MibTable
genPortTable = _GenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1)
)
if mibBuilder.loadTexts:
    genPortTable.setStatus("mandatory")
_GenPortEntry_Object = MibTableRow
genPortEntry = _GenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1)
)
genPortEntry.setIndexNames(
    (0, "LANNET-MIB", "genPortGroupId"),
    (0, "LANNET-MIB", "genPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 2),
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("clock", 14),
          ("dte", 16),
          ("fddi", 13),
          ("foirl", 6),
          ("genTokenRing", 15),
          ("lobe", 8),
          ("localTalk", 12),
          ("private", 1),
          ("repeater10BaseT", 4),
          ("repeaterAUI", 2),
          ("repeaterThin", 3),
          ("ri", 9),
          ("ro", 10),
          ("serial", 11),
          ("tenBaseFSyncAct", 5),
          ("xcvr", 7))
    )


_GenPortFunctionality_Type.__name__ = "Integer32"
_GenPortFunctionality_Object = MibTableColumn
genPortFunctionality = _GenPortFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 3),
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
          ("ielb-10btPort", 30),
          ("ielb-AUIPort", 29),
          ("itlbDTEPort", 38),
          ("itlbRiPort", 37),
          ("itlbRoPort", 36),
          ("le10bPort", 1),
          ("le10bnPort", 40),
          ("le10cPort", 2),
          ("le110bPort", 45),
          ("le110bqPort", 46),
          ("le120rPort", 41),
          ("le140xtPort", 28),
          ("le140xtcPort", 44),
          ("le140xtf-10btPort", 43),
          ("le140xtf-foPort", 42),
          ("le140xtf-fofbPort", 56),
          ("le140xtnPort", 75),
          ("le140xtqPort", 47),
          ("le15Port", 3),
          ("le20Port", 4),
          ("le20fbPort", 55),
          ("le20rPort", 35),
          ("le30xPort", 5),
          ("le30xdPort", 6),
          ("le40xPort", 7),
          ("le40xtPort", 8),
          ("le80xtPort", 27),
          ("lert40-10btPort", 49),
          ("lert40-AUIPort", 48),
          ("llt8Port", 34),
          ("lobe104RJ45S", 54),
          ("lobeD25", 11),
          ("lobeD9", 10),
          ("lobeFO", 12),
          ("lobeRJ45", 9),
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
          ("starFO", 39),
          ("unknownPort", 255))
    )


_GenPortType_Type.__name__ = "Integer32"
_GenPortType_Object = MibTableColumn
genPortType = _GenPortType_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 4),
    _GenPortType_Type()
)
genPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortType.setStatus("mandatory")


class _GenPortDescr_Type(OctetString):
    """Custom type genPortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenPortDescr_Type.__name__ = "OctetString"
_GenPortDescr_Object = MibTableColumn
genPortDescr = _GenPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 6),
    _GenPortActivityStatus_Type()
)
genPortActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortActivityStatus.setStatus("mandatory")
_GenPortSecurityPolicy_Type = OctetString
_GenPortSecurityPolicy_Object = MibTableColumn
genPortSecurityPolicy = _GenPortSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 7),
    _GenPortSecurityPolicy_Type()
)
genPortSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genPortSecurityPolicy.setStatus("mandatory")
_GenPortSecureAddresses_Type = OctetString
_GenPortSecureAddresses_Object = MibTableColumn
genPortSecureAddresses = _GenPortSecureAddresses_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 10),
    _GenPortAdminStatus_Type()
)
genPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genPortAdminStatus.setStatus("mandatory")
_GenPortSpecificOID_Type = ObjectIdentifier
_GenPortSpecificOID_Object = MibTableColumn
genPortSpecificOID = _GenPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 9, 1, 1, 11),
    _GenPortSpecificOID_Type()
)
genPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortSpecificOID.setStatus("mandatory")
_GenIntPort_ObjectIdentity = ObjectIdentity
genIntPort = _GenIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 10)
)
_GenIntPortTable_Object = MibTable
genIntPortTable = _GenIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 10, 1)
)
if mibBuilder.loadTexts:
    genIntPortTable.setStatus("mandatory")
_GenIntPortEntry_Object = MibTableRow
genIntPortEntry = _GenIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1)
)
genIntPortEntry.setIndexNames(
    (0, "LANNET-MIB", "genIntPortGroupId"),
    (0, "LANNET-MIB", "genIntPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 4),
    _GenIntPortActivityStatus_Type()
)
genIntPortActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortActivityStatus.setStatus("mandatory")


class _GenIntPortBusConnNumber_Type(Integer32):
    """Custom type genIntPortBusConnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenIntPortBusConnNumber_Type.__name__ = "Integer32"
_GenIntPortBusConnNumber_Object = MibTableColumn
genIntPortBusConnNumber = _GenIntPortBusConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 5),
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 4),
          ("local-talk", 3),
          ("other", 255),
          ("token-ring", 2))
    )


_GenIntPortBusConnType_Type.__name__ = "Integer32"
_GenIntPortBusConnType_Object = MibTableColumn
genIntPortBusConnType = _GenIntPortBusConnType_Object(
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 6),
    _GenIntPortBusConnType_Type()
)
genIntPortBusConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortBusConnType.setStatus("mandatory")
_GenIntPortSpecificOID_Type = ObjectIdentifier
_GenIntPortSpecificOID_Object = MibTableColumn
genIntPortSpecificOID = _GenIntPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 10, 1, 1, 7),
    _GenIntPortSpecificOID_Type()
)
genIntPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortSpecificOID.setStatus("mandatory")
_SoftRedundancy_ObjectIdentity = ObjectIdentity
softRedundancy = _SoftRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 11)
)
_SoftRedundancyTable_Object = MibTable
softRedundancyTable = _SoftRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 11, 1)
)
if mibBuilder.loadTexts:
    softRedundancyTable.setStatus("mandatory")
_SoftRedundancyEntry_Object = MibTableRow
softRedundancyEntry = _SoftRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1)
)
softRedundancyEntry.setIndexNames(
    (0, "LANNET-MIB", "softRedundancyId"),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 1),
    _SoftRedundancyId_Type()
)
softRedundancyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softRedundancyId.setStatus("mandatory")


class _SoftRedundancyName_Type(OctetString):
    """Custom type softRedundancyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_SoftRedundancyName_Type.__name__ = "OctetString"
_SoftRedundancyName_Object = MibTableColumn
softRedundancyName = _SoftRedundancyName_Object(
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 11, 1, 1, 7),
    _SoftRedundancyStatus_Type()
)
softRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyStatus.setStatus("mandatory")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12)
)
_EthAg_ObjectIdentity = ObjectIdentity
ethAg = _EthAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 1)
)
_EthAgTable_Object = MibTable
ethAgTable = _EthAgTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ethAgTable.setStatus("mandatory")
_EthAgEntry_Object = MibTableRow
ethAgEntry = _EthAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1)
)
ethAgEntry.setIndexNames(
    (0, "LANNET-MIB", "ethAgId"),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1, 1),
    _EthAgId_Type()
)
ethAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAgId.setStatus("mandatory")
_EthAgPerfBusSelection_Type = Integer32
_EthAgPerfBusSelection_Object = MibTableColumn
ethAgPerfBusSelection = _EthAgPerfBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 1, 1, 1, 2),
    _EthAgPerfBusSelection_Type()
)
ethAgPerfBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAgPerfBusSelection.setStatus("mandatory")
_EthGroup_ObjectIdentity = ObjectIdentity
ethGroup = _EthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 2)
)
_EthGroupTable_Object = MibTable
ethGroupTable = _EthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ethGroupTable.setStatus("mandatory")
_EthGroupEntry_Object = MibTableRow
ethGroupEntry = _EthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1)
)
ethGroupEntry.setIndexNames(
    (0, "LANNET-MIB", "ethGroupId"),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 9),
    _EthGroupSingleBusMode_Type()
)
ethGroupSingleBusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSingleBusMode.setStatus("mandatory")
_EthGroupSpecificOID_Type = ObjectIdentifier
_EthGroupSpecificOID_Object = MibTableColumn
ethGroupSpecificOID = _EthGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 2, 1, 1, 10),
    _EthGroupSpecificOID_Type()
)
ethGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSpecificOID.setStatus("mandatory")
_EthPort_ObjectIdentity = ObjectIdentity
ethPort = _EthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 3)
)
_EthPortTable_Object = MibTable
ethPortTable = _EthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ethPortTable.setStatus("mandatory")
_EthPortEntry_Object = MibTableRow
ethPortEntry = _EthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1)
)
ethPortEntry.setIndexNames(
    (0, "LANNET-MIB", "ethPortGroupId"),
    (0, "LANNET-MIB", "ethPortId"),
)
if mibBuilder.loadTexts:
    ethPortEntry.setStatus("mandatory")
_EthPortGroupId_Type = Integer32
_EthPortGroupId_Object = MibTableColumn
ethPortGroupId = _EthPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 1),
    _EthPortGroupId_Type()
)
ethPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortGroupId.setStatus("mandatory")
_EthPortId_Type = Integer32
_EthPortId_Object = MibTableColumn
ethPortId = _EthPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 10),
    _EthPortSQETest_Type()
)
ethPortSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortSQETest.setStatus("mandatory")
_EthPortLastSourceAddr_Type = OctetString
_EthPortLastSourceAddr_Object = MibTableColumn
ethPortLastSourceAddr = _EthPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 12),
    _EthPortUserStatus_Type()
)
ethPortUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortUserStatus.setStatus("mandatory")
_EthPortMainBusSelection_Type = Integer32
_EthPortMainBusSelection_Object = MibTableColumn
ethPortMainBusSelection = _EthPortMainBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 13),
    _EthPortMainBusSelection_Type()
)
ethPortMainBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortMainBusSelection.setStatus("mandatory")
_EthPortTraffic_Type = Counter32
_EthPortTraffic_Object = MibTableColumn
ethPortTraffic = _EthPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 14),
    _EthPortTraffic_Type()
)
ethPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortTraffic.setStatus("mandatory")
_EthPortFramesReceivedOK_Type = Counter32
_EthPortFramesReceivedOK_Object = MibTableColumn
ethPortFramesReceivedOK = _EthPortFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 15),
    _EthPortFramesReceivedOK_Type()
)
ethPortFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFramesReceivedOK.setStatus("mandatory")
_EthPortRunts_Type = Counter32
_EthPortRunts_Object = MibTableColumn
ethPortRunts = _EthPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 16),
    _EthPortRunts_Type()
)
ethPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortRunts.setStatus("mandatory")
_EthPortPacketErrors_Type = Counter32
_EthPortPacketErrors_Object = MibTableColumn
ethPortPacketErrors = _EthPortPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 17),
    _EthPortPacketErrors_Type()
)
ethPortPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPacketErrors.setStatus("mandatory")
_EthPortSpecificOID_Type = ObjectIdentifier
_EthPortSpecificOID_Object = MibTableColumn
ethPortSpecificOID = _EthPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 3, 1, 1, 18),
    _EthPortSpecificOID_Type()
)
ethPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortSpecificOID.setStatus("mandatory")
_EthIntPort_ObjectIdentity = ObjectIdentity
ethIntPort = _EthIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 4)
)
_EthIntPortTable_Object = MibTable
ethIntPortTable = _EthIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ethIntPortTable.setStatus("mandatory")
_EthIntPortEntry_Object = MibTableRow
ethIntPortEntry = _EthIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1)
)
ethIntPortEntry.setIndexNames(
    (0, "LANNET-MIB", "ethIntPortGroupId"),
    (0, "LANNET-MIB", "ethIntPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 4, 1, 1, 5),
    _EthIntPortBackedUp_Type()
)
ethIntPortBackedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIntPortBackedUp.setStatus("mandatory")
_EthBus_ObjectIdentity = ObjectIdentity
ethBus = _EthBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 12, 5)
)
_EthBusPerfTable_Object = MibTable
ethBusPerfTable = _EthBusPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ethBusPerfTable.setStatus("mandatory")
_EthBusPerfEntry_Object = MibTableRow
ethBusPerfEntry = _EthBusPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1)
)
ethBusPerfEntry.setIndexNames(
    (0, "LANNET-MIB", "ethBusPerfAgId"),
    (0, "LANNET-MIB", "ethBusPerfId"),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 2),
    _EthBusPerfId_Type()
)
ethBusPerfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPerfId.setStatus("mandatory")
_EthBusTrafficBuffer_Type = OctetString
_EthBusTrafficBuffer_Object = MibTableColumn
ethBusTrafficBuffer = _EthBusTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 3),
    _EthBusTrafficBuffer_Type()
)
ethBusTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTrafficBuffer.setStatus("mandatory")
_EthBusTrafficThresh_Type = Integer32
_EthBusTrafficThresh_Object = MibTableColumn
ethBusTrafficThresh = _EthBusTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 4),
    _EthBusTrafficThresh_Type()
)
ethBusTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBusTrafficThresh.setStatus("mandatory")
_EthBusPeakTraffic_Type = Integer32
_EthBusPeakTraffic_Object = MibTableColumn
ethBusPeakTraffic = _EthBusPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 5),
    _EthBusPeakTraffic_Type()
)
ethBusPeakTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPeakTraffic.setStatus("mandatory")
_EthBusTotalCollisions_Type = Counter32
_EthBusTotalCollisions_Object = MibTableColumn
ethBusTotalCollisions = _EthBusTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 6),
    _EthBusTotalCollisions_Type()
)
ethBusTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalCollisions.setStatus("mandatory")
_EthBusTotalPackets_Type = Counter32
_EthBusTotalPackets_Object = MibTableColumn
ethBusTotalPackets = _EthBusTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 7),
    _EthBusTotalPackets_Type()
)
ethBusTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalPackets.setStatus("mandatory")
_EthBusTotalErrors_Type = Counter32
_EthBusTotalErrors_Object = MibTableColumn
ethBusTotalErrors = _EthBusTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 8),
    _EthBusTotalErrors_Type()
)
ethBusTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalErrors.setStatus("mandatory")
_EthBusTraffic_Type = Integer32
_EthBusTraffic_Object = MibTableColumn
ethBusTraffic = _EthBusTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 1, 1, 9),
    _EthBusTraffic_Type()
)
ethBusTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTraffic.setStatus("mandatory")
_EthBusClockTable_Object = MibTable
ethBusClockTable = _EthBusClockTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2)
)
if mibBuilder.loadTexts:
    ethBusClockTable.setStatus("mandatory")
_EthBusClockEntry_Object = MibTableRow
ethBusClockEntry = _EthBusClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1)
)
ethBusClockEntry.setIndexNames(
    (0, "LANNET-MIB", "ethBusClockBusId"),
    (0, "LANNET-MIB", "ethBusClockId"),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 12, 5, 2, 1, 3),
    _EthBusClockTestResult_Type()
)
ethBusClockTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockTestResult.setStatus("mandatory")
_Tok_ObjectIdentity = ObjectIdentity
tok = _Tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13)
)
_TokRing_ObjectIdentity = ObjectIdentity
tokRing = _TokRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 1)
)
_TokRingTable_Object = MibTable
tokRingTable = _TokRingTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tokRingTable.setStatus("mandatory")
_TokRingEntry_Object = MibTableRow
tokRingEntry = _TokRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1)
)
tokRingEntry.setIndexNames(
    (0, "LANNET-MIB", "tokRingAgId"),
    (0, "LANNET-MIB", "tokRingId"),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 4),
    _TokRingRightSlot_Type()
)
tokRingRightSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingRightSlot.setStatus("mandatory")
_TokRingTrafficBuffer_Type = OctetString
_TokRingTrafficBuffer_Object = MibTableColumn
tokRingTrafficBuffer = _TokRingTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 5),
    _TokRingTrafficBuffer_Type()
)
tokRingTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTrafficBuffer.setStatus("mandatory")
_TokRingTrafficThresh_Type = Integer32
_TokRingTrafficThresh_Object = MibTableColumn
tokRingTrafficThresh = _TokRingTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 6),
    _TokRingTrafficThresh_Type()
)
tokRingTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingTrafficThresh.setStatus("mandatory")
_TokRingPeakTraffic_Type = Integer32
_TokRingPeakTraffic_Object = MibTableColumn
tokRingPeakTraffic = _TokRingPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 7),
    _TokRingPeakTraffic_Type()
)
tokRingPeakTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingPeakTraffic.setStatus("mandatory")
_TokRingNumberOfStations_Type = Integer32
_TokRingNumberOfStations_Object = MibTableColumn
tokRingNumberOfStations = _TokRingNumberOfStations_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 8),
    _TokRingNumberOfStations_Type()
)
tokRingNumberOfStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingNumberOfStations.setStatus("mandatory")
_TokRingConfiguration_Type = OctetString
_TokRingConfiguration_Object = MibTableColumn
tokRingConfiguration = _TokRingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 10),
    _TokRingBeaconing_Type()
)
tokRingBeaconing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingBeaconing.setStatus("mandatory")
_TokRingBeaconingStation_Type = OctetString
_TokRingBeaconingStation_Object = MibTableColumn
tokRingBeaconingStation = _TokRingBeaconingStation_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 12),
    _TokRingStationsMatch_Type()
)
tokRingStationsMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationsMatch.setStatus("mandatory")
_TokRingTraffic_Type = Integer32
_TokRingTraffic_Object = MibTableColumn
tokRingTraffic = _TokRingTraffic_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 1, 1, 1, 13),
    _TokRingTraffic_Type()
)
tokRingTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTraffic.setStatus("mandatory")
_TokGroup_ObjectIdentity = ObjectIdentity
tokGroup = _TokGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 2)
)
_TokGroupTable_Object = MibTable
tokGroupTable = _TokGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tokGroupTable.setStatus("mandatory")
_TokGroupEntry_Object = MibTableRow
tokGroupEntry = _TokGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1)
)
tokGroupEntry.setIndexNames(
    (0, "LANNET-MIB", "tokGroupId"),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 13),
    _TokGroupAutoBusLoop_Type()
)
tokGroupAutoBusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoBusLoop.setStatus("mandatory")
_TokGroupSpecificOID_Type = ObjectIdentifier
_TokGroupSpecificOID_Object = MibTableColumn
tokGroupSpecificOID = _TokGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 1, 1, 14),
    _TokGroupSpecificOID_Type()
)
tokGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupSpecificOID.setStatus("mandatory")
_TokGroupRingTable_Object = MibTable
tokGroupRingTable = _TokGroupRingTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2)
)
if mibBuilder.loadTexts:
    tokGroupRingTable.setStatus("mandatory")
_TokGroupRingEntry_Object = MibTableRow
tokGroupRingEntry = _TokGroupRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1)
)
tokGroupRingEntry.setIndexNames(
    (0, "LANNET-MIB", "tokGroupRingGroupId"),
    (0, "LANNET-MIB", "tokGroupRingId"),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 2),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("unknown", 1))
    )


_TokGroupRingSpeed_Type.__name__ = "Integer32"
_TokGroupRingSpeed_Object = MibTableColumn
tokGroupRingSpeed = _TokGroupRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 2, 2, 1, 4),
    _TokGroupRingInserted_Type()
)
tokGroupRingInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingInserted.setStatus("mandatory")
_TokPort_ObjectIdentity = ObjectIdentity
tokPort = _TokPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 13, 3)
)
_TokPortTable_Object = MibTable
tokPortTable = _TokPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1)
)
if mibBuilder.loadTexts:
    tokPortTable.setStatus("mandatory")
_TokPortEntry_Object = MibTableRow
tokPortEntry = _TokPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1)
)
tokPortEntry.setIndexNames(
    (0, "LANNET-MIB", "tokPortGroupId"),
    (0, "LANNET-MIB", "tokPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 7),
    _TokPortFunctionalStatus_Type()
)
tokPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortFunctionalStatus.setStatus("mandatory")
_TokPortLastSourceAddr_Type = OctetString
_TokPortLastSourceAddr_Object = MibTableColumn
tokPortLastSourceAddr = _TokPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 8),
    _TokPortLastSourceAddr_Type()
)
tokPortLastSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortLastSourceAddr.setStatus("mandatory")
_TokPortSpecificOID_Type = ObjectIdentifier
_TokPortSpecificOID_Object = MibTableColumn
tokPortSpecificOID = _TokPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 81, 13, 3, 1, 1, 9),
    _TokPortSpecificOID_Type()
)
tokPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortSpecificOID.setStatus("mandatory")
_Ts_ObjectIdentity = ObjectIdentity
ts = _Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 14)
)
_TsGroup_ObjectIdentity = ObjectIdentity
tsGroup = _TsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 14, 1)
)
_TsGroupTable_Object = MibTable
tsGroupTable = _TsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tsGroupTable.setStatus("mandatory")
_TsGroupEntry_Object = MibTableRow
tsGroupEntry = _TsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1)
)
tsGroupEntry.setIndexNames(
    (0, "LANNET-MIB", "tsGroupId"),
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
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 14, 1, 1, 1, 3),
    _TsGroupOperationMode_Type()
)
tsGroupOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupOperationMode.setStatus("mandatory")
_Ltalk_ObjectIdentity = ObjectIdentity
ltalk = _Ltalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 15)
)
_LtalkPort_ObjectIdentity = ObjectIdentity
ltalkPort = _LtalkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 15, 1)
)
_LtalkPortTable_Object = MibTable
ltalkPortTable = _LtalkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ltalkPortTable.setStatus("mandatory")
_LtalkPortEntry_Object = MibTableRow
ltalkPortEntry = _LtalkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1)
)
ltalkPortEntry.setIndexNames(
    (0, "LANNET-MIB", "ltalkPortGroupId"),
    (0, "LANNET-MIB", "ltalkPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 81, 15, 1, 1, 1, 5),
    _LtalkPortJam_Type()
)
ltalkPortJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortJam.setStatus("mandatory")
_Cl_ObjectIdentity = ObjectIdentity
cl = _Cl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16)
)
_ClGroup_ObjectIdentity = ObjectIdentity
clGroup = _ClGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16, 1)
)
_ClGroupTable_Object = MibTable
clGroupTable = _ClGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1)
)
if mibBuilder.loadTexts:
    clGroupTable.setStatus("mandatory")
_ClGroupEntry_Object = MibTableRow
clGroupEntry = _ClGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1)
)
clGroupEntry.setIndexNames(
    (0, "LANNET-MIB", "clGroupId"),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 2),
    _ClGroupClockRedundancy_Type()
)
clGroupClockRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupClockRedundancy.setStatus("mandatory")
_ClGroupMainClock_Type = Integer32
_ClGroupMainClock_Object = MibTableColumn
clGroupMainClock = _ClGroupMainClock_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 1, 1, 1, 4),
    _ClGroupTestClocks_Type()
)
clGroupTestClocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupTestClocks.setStatus("mandatory")
_ClPort_ObjectIdentity = ObjectIdentity
clPort = _ClPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 16, 2)
)
_ClPortTable_Object = MibTable
clPortTable = _ClPortTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1)
)
if mibBuilder.loadTexts:
    clPortTable.setStatus("mandatory")
_ClPortEntry_Object = MibTableRow
clPortEntry = _ClPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1)
)
clPortEntry.setIndexNames(
    (0, "LANNET-MIB", "clPortGroupId"),
    (0, "LANNET-MIB", "clPortId"),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 81, 16, 2, 1, 1, 3),
    _ClPortFunctionalStatus_Type()
)
clPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortFunctionalStatus.setStatus("mandatory")
_LntOID_ObjectIdentity = ObjectIdentity
lntOID = _LntOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17)
)
_LBoxOID_ObjectIdentity = ObjectIdentity
lBoxOID = _LBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1)
)
_LUnknownBoxOID_ObjectIdentity = ObjectIdentity
lUnknownBoxOID = _LUnknownBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 1)
)
_LLET18BoxOID_ObjectIdentity = ObjectIdentity
lLET18BoxOID = _LLET18BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 2)
)
_LLET3BoxOID_ObjectIdentity = ObjectIdentity
lLET3BoxOID = _LLET3BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 3)
)
_LLET36BoxOID_ObjectIdentity = ObjectIdentity
lLET36BoxOID = _LLET36BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 4)
)
_LLET18EBoxOID_ObjectIdentity = ObjectIdentity
lLET18EBoxOID = _LLET18EBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 5)
)
_LLERT40BoxOID_ObjectIdentity = ObjectIdentity
lLERT40BoxOID = _LLERT40BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 6)
)
_LLET10BoxOID_ObjectIdentity = ObjectIdentity
lLET10BoxOID = _LLET10BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 7)
)
_LFDX100BoxOID_ObjectIdentity = ObjectIdentity
lFDX100BoxOID = _LFDX100BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANNET-MIB",
    **{"lannet": lannet,
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
       "chLntAgTable": chLntAgTable,
       "chLntAgEntry": chLntAgEntry,
       "chLntAgId": chLntAgId,
       "chLntAgSLIPAddress": chLntAgSLIPAddress,
       "chLntAgSWVersion": chLntAgSWVersion,
       "chLntAgKernelVersion": chLntAgKernelVersion,
       "chLntAgCoprocSWVersion": chLntAgCoprocSWVersion,
       "chLntAgSWFault": chLntAgSWFault,
       "chLntAgMgmtBusSelection": chLntAgMgmtBusSelection,
       "chLntAgCoprocCommStatus": chLntAgCoprocCommStatus,
       "chLntAgCommDebugMode": chLntAgCommDebugMode,
       "chLntAgConfigChangeTraps": chLntAgConfigChangeTraps,
       "chLntAgFaultTraps": chLntAgFaultTraps,
       "chLntAgTrafficThreshTraps": chLntAgTrafficThreshTraps,
       "chLntAgGroupEnrollDeenrollTraps": chLntAgGroupEnrollDeenrollTraps,
       "chLntAgSoftFaultTraps": chLntAgSoftFaultTraps,
       "chLntAgHubEnrollTraps": chLntAgHubEnrollTraps,
       "chLntAgTempThreshTraps": chLntAgTempThreshTraps,
       "chLntAgSpecificOID": chLntAgSpecificOID,
       "chLntAgLastAddrConfig": chLntAgLastAddrConfig,
       "chLntAgSecAddrConfig": chLntAgSecAddrConfig,
       "chLntAgSoftwareStatus": chLntAgSoftwareStatus,
       "chLntAgConfigurationSymbol": chLntAgConfigurationSymbol,
       "chLntAgIntTemp": chLntAgIntTemp,
       "chLntAgBootVersion": chLntAgBootVersion,
       "chMgr": chMgr,
       "chMgrTrapRepStatus": chMgrTrapRepStatus,
       "chMgrContPerfRep": chMgrContPerfRep,
       "chMgrMngmtState": chMgrMngmtState,
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
       "lntOID": lntOID,
       "lBoxOID": lBoxOID,
       "lUnknownBoxOID": lUnknownBoxOID,
       "lLET18BoxOID": lLET18BoxOID,
       "lLET3BoxOID": lLET3BoxOID,
       "lLET36BoxOID": lLET36BoxOID,
       "lLET18EBoxOID": lLET18EBoxOID,
       "lLERT40BoxOID": lLERT40BoxOID,
       "lLET10BoxOID": lLET10BoxOID,
       "lFDX100BoxOID": lFDX100BoxOID}
)
